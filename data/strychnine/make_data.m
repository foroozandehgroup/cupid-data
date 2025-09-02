% Simulate 2DJ for strychnine

global MAGNET OFFSET SWEEP_F1 SWEEP_F2 NPOINTS_F1 NPOINTS_F2 TAU_C;

MAGNET = 11.74;
OFFSET = 2500;
SWEEP_F1 = 50;
SWEEP_F2 = 5000;
NPOINTS_F1 = 128;
NPOINTS_F2 = 8192;
TAU_C = 200e-12;  % 200ps

fid = make_2dj();
save("fid.mat", "fid");

function bas = get_bas()
    bas.formalism = 'sphten-liouv';
    bas.approximation = 'IK-2';
    bas.connectivity = 'scalar_couplings';
    bas.space_level = 1;
end

function spin_system = configure(sys, inter, bas)
    global MAGNET;
    sys.magnet = MAGNET;
    inter = configure_relaxtion(inter);
    spin_system=create(sys, inter);
    spin_system=basis(spin_system, bas);
end

function inter = configure_relaxtion(inter)
    global TAU_C;
    inter.relaxation = {'redfield'};
    inter.equilibrium = 'zero';
    inter.rlx_keep = 'secular';
    inter.tau_c = {TAU_C};
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
