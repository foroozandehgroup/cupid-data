from collections import deque
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import subprocess
import tomli_w
from typing import ClassVar, Self

import numpy as np
from numpy.random import Generator


@dataclass
class Dataset:

    shifts: list[float]
    couplings: list[tuple[int, int, float]]
    sfo: float
    sw: tuple[float, float]
    offset: float
    pts: tuple[int, int]

    @classmethod
    def new(
        cls,
        rng: Generator,
        n_spins: int,
        n_couplings: int,
        min_shift: float,
        max_shift: float,
        min_coupling: float,
        max_coupling: float,
        sfo: float,
        sw: tuple[float, float],
        offset: float,
        pts: tuple[int, int],
    ) -> Self:
        min_coupling_spin_shift = 10.0 * max_shift
        max_coupling_spin_shift = (offset + 0.5 * sw[1])
        assert min_coupling_spin_shift < max_coupling_spin_shift

        f1_res = sw[0] / pts[0]
        f2_res = (sw[1] / pts[1]) / sfo
        while True:
            shifts = sorted((rng.uniform(min_shift, max_shift, size=n_spins) / sfo).tolist())
            if cls._check_too_close(shifts, f2_res):
                continue

            couplings = []
            for i in range(n_spins):
                while True:
                    new_couplings = rng.uniform(
                        min_coupling, max_coupling, size=n_couplings,
                    ).tolist()
                    if cls._check_too_close(
                        cls._get_multiplet_freqs(new_couplings),
                        f1_res,
                    ):
                        continue
                    couplings.extend(
                        [
                            (i + 1, n_spins + j + 1, c)
                            for j, c in enumerate(new_couplings)
                        ]
                    )
                    break
            break

        shifts.extend(
            (
                rng.uniform(
                min_coupling_spin_shift,
                max_coupling_spin_shift,
                size=n_couplings,
                ) / sfo
            ).tolist()
        )

        return cls(shifts, couplings, sfo, sw, offset, pts)

    @property
    def shift_and_coupling_info(self) -> dict:
        shift_info = {}
        coupling_info = {}
        for i, shift in enumerate(self.shifts[:4], start=1):
            shift_info[str(i)] = "{:.4f}".format(self.sfo * shift)
            cinfo = {}
            for i1, i2, coupling in self.couplings:
                if i == i1:
                    cinfo[str(i2)] = "{:.4f}".format(coupling)
            coupling_info[str(i)] = cinfo
        info = {"shifts": shift_info, "couplings": coupling_info}
        return info

    def func_call_str(self, savepath: Path) -> str:
        return "make_data({}, {}, {}, {}, {}, {}, '{}');".format(
            self.shifts_matlab_str,
            self.couplings_matlab_str,
            self.sfo,
            self.sw_matlab_str,
            self.offset,
            self.pts_matlab_str,
            savepath,
        )

    @property
    def shifts_matlab_str(self) -> str:
        return "[{}]".format(" ".join(["{:.4f}".format(shift) for shift in self.shifts]))

    @property
    def couplings_matlab_str(self) -> str:
        ss = []
        for i1, i2, coupling in self.couplings:
            ss.append("{} {} {:.4f}".format(i1, i2, coupling))
        return "[{}]".format("; ".join(ss))

    @property
    def sw_matlab_str(self) -> str:
        return "[{} {}]".format(self.sw[0], self.sw[1])

    @property
    def pts_matlab_str(self) -> str:
        return "[{} {}]".format(self.pts[0], self.pts[1])


    @staticmethod
    def _check_too_close(lst: list[float], threshold: float) -> bool:
        for f1, f2 in combinations(lst, 2):
            if abs(f1 - f2) <= threshold:
                return True
        return False

    @staticmethod
    def _get_multiplet_freqs(couplings: list[float]) -> list[float]:
        freqs = deque([0.0])
        for coupling in couplings:
            n = len(freqs)
            for _ in range(n):
                f = freqs.popleft()
                freqs.append(f - coupling / 2)
                freqs.append(f + coupling / 2)

        freqs = sorted(freqs)
        return freqs


@dataclass
class Datasets:

    MATLAB: ClassVar[str] = "/home/simonhulse/progs/MATLAB/R2024b/bin/matlab"
    CMD_TMPL: ClassVar[str] = "{} -nodisplay -nodesktop -r \"{} exit;\""

    datasets: list[Dataset]

    def run_spinach(self, outdir: Path) -> None:
        outdir.mkdir(exist_ok=True)
        func_call_strs = []
        for i, ds in enumerate(self.datasets, start=1):
            savepath = outdir / "dataset_{}.mat".format(i)
            func_call_strs.append(ds.func_call_str(savepath))
        func_calls = " ".join(func_call_strs)
        cmd = self.CMD_TMPL.format(self.MATLAB, func_calls)
        subprocess.run(cmd, shell=True)

    @property
    def shift_and_coupling_info(self) -> str:
        info = {}
        for i, dataset in enumerate(self.datasets, start=1):
            info["estimator_{}".format(i)] = dataset.shift_and_coupling_info
        toml = tomli_w.dumps(info)
        return toml


def main():
    outdir = Path(__file__).parent / "datasets"

    rng = np.random.default_rng(0)
    n_datasets = 5
    n_spins = 4
    n_couplings = 3
    sfo = 500.
    sw = (40., 1000.)
    offset = 0.
    pts = (128, 1024)

    min_coupling = 1.0
    max_coupling = 10.0
    min_shift = -15.0
    max_shift = 15.0

    datasets = Datasets(
        [
            Dataset.new(
                rng,
                n_spins,
                n_couplings,
                min_shift,
                max_shift,
                min_coupling,
                max_coupling,
                sfo,
                sw,
                offset,
                pts,
            )
            for _ in range(n_datasets)
        ]
    )

    datasets.run_spinach(outdir)

    with open(outdir / "dataset_info.toml", "w") as fh:
        fh.write(datasets.shift_and_coupling_info)


if __name__ == "__main__":
    main()
