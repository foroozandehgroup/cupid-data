% Simulate 2DJ datasets for strychnine

global MAGNET OFFSET SWEEP_F1 SWEEP_F2 NPOINTS_F1 NPOINTS_F2;

MAGNET = 11.74;
OFFSET = 2500;
SWEEP_F1 = 50;
SWEEP_F2 = 5000;
NPOINTS_F1 = 128;
NPOINTS_F2 = 8192;

fid_2dj = make_2dj();
save("fid_2dj.mat", "fid_2dj");
clear fid_2dj;
fid_pure_shift = make_pure_shift();
save("fid_pure_shift.mat", "fid_pure_shift");
clear fid_pure_shift;

function bas = get_bas()
    bas.formalism = 'sphten-liouv';
    bas.approximation = 'IK-2';
    bas.connectivity = 'scalar_couplings';
    bas.space_level = 1;
end

function spin_system = configure(sys, inter, bas)
    global MAGNET;
    sys.magnet = MAGNET;
    spin_system=create(sys, inter);
    spin_system=basis(spin_system, bas);
end

function fid = make_2dj()
    global OFFSET SWEEP_F1 SWEEP_F2 NPOINTS_F1 NPOINTS_F2;
    parameters.offset = OFFSET;
    parameters.sweep = [SWEEP_F1 SWEEP_F2];
    parameters.npoints = [NPOINTS_F1 NPOINTS_F2];
    parameters.spins = {'1H'};

    bas = get_bas();

    [sys,inter] = strychnine({'1H'});
    spin_system = configure(sys, inter, bas);
    fid = liquid(spin_system, @jres_seq, parameters, 'nmr');
end

function fid = make_pure_shift()
    global OFFSET SWEEP_F2 NPOINTS_F2;

    [sys,inter] = strychnine({'1H'});
    bas = get_bas();
    spin_system = configure(sys, inter, bas);
    sys.inter.coupling.scalar = cell(22, 22);
    sys.inter.coupling.scalar(:) = {0.0};

    parameters.rho0 = state(spin_system, 'L+', '1H', 'cheap');
    parameters.coil = state(spin_system, 'L+', '1H', 'cheap');
    parameters.offset = OFFSET;
    parameters.sweep = SWEEP_F2;
    parameters.npoints = NPOINTS_F2;
    parameters.spins = {'1H'};

    fid = liquid(spin_system, @acquire, parameters, 'nmr');
end
