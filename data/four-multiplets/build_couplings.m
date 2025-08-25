function couplings = build_couplings(n_spins, cinfo)
    disp(cinfo);
    couplings = cell(n_spins, n_spins);
    nrows = size(cinfo, 1);
    disp(nrows);
    for i = 1:nrows
        index_1 = cinfo(i, 1);
        index_2 = cinfo(i, 2);
        coupling = cinfo(i, 3);
        couplings{index_1, index_2} = coupling;
    end
    celldisp(couplings);
end
