function make_data(shifts, couplings, sfo, sw, offset, pts, savepath)
    field = get_field(sfo, offset);
    sys.magnet = field;
    n_spins = length(shifts);
    sys.isotopes = build_isotopes(n_spins);

    % Interactions
    inter.zeeman.scalar = num2cell(shifts);
    inter.coupling.scalar = build_couplings(n_spins, couplings);

    % Relaxation theory parameters
    inter.relaxation={'redfield'};
    inter.equilibrium='zero';
    inter.rlx_keep='kite';
    inter.tau_c={200e-12};

    % Basis set
    bas.formalism = 'sphten-liouv';
    bas.approximation = 'IK-2';
    bas.connectivity = 'scalar_couplings';
    bas.space_level = 1;

    % Spinach housekeeping
    spin_system = create(sys, inter);
    spin_system = basis(spin_system, bas);

    % Sequence parameters
    parameters.offset = offset;
    parameters.sweep = sw;
    parameters.npoints = pts;
    parameters.spins = {'1H'};

    fid = liquid(spin_system, @jres_seq, parameters, 'nmr');
    save(savepath, "fid");
end

function field = get_field(sfo, offset)
    gamma = spin('1H');
    field = (2*pi * (1e6 * sfo - offset)) / gamma;
end

function isotopes = build_isotopes(n_spins)
    isotopes = cell(n_spins, 1);
    for i = 1:n_spins
        isotopes{i} = '1H';
    end
end

function couplings = build_couplings(n_spins, cinfo)
    couplings = cell(n_spins, n_spins);
    nrows = size(cinfo, 1);
    for i = 1:nrows
        index_1 = cinfo(i, 1);
        index_2 = cinfo(i, 2);
        coupling = cinfo(i, 3);
        couplings{index_1, index_2} = coupling;
    end
end
