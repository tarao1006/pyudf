import json

from .utils import find_file, deepupdate
from .udftype import particle, sparticle, matrix3d, vector3d
from .formatter import Formatter


class Udf(Formatter):
    """Udf class.

    Attributs
    ---------
    constitutive_eq: dict
    object_type: dict
    a_xi: float
    a: float
    gravity: dict
    epsilon: float
    lj_powers: dict
    mesh: dict
    time_increment: dict
    swith: dict
    output: dict
    resume: dict
        These are parameters of kapsel. For v3.4 only.

    params: dict
        Keys are valid for gourmet
    params_keys: list of str
        Keys holds order of params.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = dict(
            constitutive_eq=dict(
                type='Navier_Stokes',
                navier_stokes=dict(
                    dx=0.0,
                    rho=0.0,
                    eta=0.0,
                    kbt=0.0,
                    alpha_v=0.0,
                    alpha_o=0.0
                ),
                shear_navier_stokes=dict(
                    dx=0.0,
                    rho=0.0,
                    eta=0.0,
                    kbt=0.0,
                    alpha_v=0.0,
                    alpha_o=0.0,
                    external_field=dict(
                        type='DC',
                        dc=dict(
                            shear_rate=0.0
                        ),
                        ac=dict(
                            shear_rate=0.0,
                            frequency=0.0
                        )
                    )
                ),
                shear_navier_stokes_lees_edwards=dict(
                    dx=0.0,
                    rho=0.0,
                    eta=0.0,
                    kbt=0.0,
                    alpha_v=0.0,
                    alpha_o=0.0,
                    external_field=dict(
                        type='DC',
                        dc=dict(
                            shear_rate=0.0
                        ),
                        ac=dict(
                            shear_rate=0.0,
                            frequency=0.0
                        )
                    )
                ),
                electrolyte=dict(
                    dx=0.0,
                    rho=0.0,
                    eta=0.0,
                    kbt=0.0,
                    alpha_v=0.0,
                    alpha_o=0.0,
                    dielectric_cst=0.0,
                    init_profile='Uniform',
                    add_salt=dict(
                        type='salt',
                        slatfree=dict(
                            valency_counterion=0.0,
                            onsager_coeff_counterion=0.0
                        ),
                        slat=dict(
                            valency_positive_ion=0.0,
                            valency_negative_ion=0.0,
                            onsager_coeff_positive_ion=0.0,
                            onsager_coeff_negative_ion=0.0,
                            debye_length=0.0
                        )
                    ),
                    electric_field=dict(
                        type='ON',
                        on=dict(
                            type='DC',
                            dc=dict(
                                ex=0.0,
                                ey=0.0,
                                ez=0.0
                            ),
                            ac=dict(
                                ex=0.0,
                                ey=0.0,
                                ez=0.0,
                                frequency=0.0
                            )
                        )
                    )
                )
            ),
            object_type=dict(
                type='spherical_particle',
                spherical_particle=dict(
                    particle_spec=list(
                        [
                            dict(
                                particle_number=0,
                                mass_ratio=0.0,
                                surface_charge=0.0,
                                janus_axis='NONE',
                                jauns_propulsion='OFF',
                                janus_force=dict(
                                    x=0.0,
                                    y=0.0,
                                    z=0.0
                                ),
                                janus_torque=dict(
                                    x=0.0,
                                    y=0.0,
                                    z=0.0
                                ),
                                janus_slip_vel=0.0,
                                janus_slip_mode=0.0,
                                janus_rotlet_c1=0.0,
                                janus_rotlet_dipolr_c2=0.0
                            )
                        ]
                    )
                ),
                chain=dict(
                    chain_spec=list(
                        [
                            dict(
                                beads_number=0,
                                chain_number=0,
                                mass_ratio=0.0,
                                surface_charge=0.0,
                                janus_axis='NONE'
                            )
                        ]
                    )
                ),
                rigid=dict(
                    rigid_specs=list(
                        [
                            dict(
                                beads_number=0,
                                chain_number=0,
                                mass_ration=0.0,
                                surface_charge=0.0,
                                rigid_motion='fix',
                                rigid_velocity=dict(
                                    x=0.0,
                                    y=0.0,
                                    z=0.0
                                ),
                                rigid_omega=dict(
                                    x=0.0,
                                    y=0.0,
                                    z=0.0
                                )
                            )
                        ]
                    )
                )
            ),
            a_xi=0.0,
            a=0.0,
            gravity=dict(
                g=0.0,
                g_direction='-X'
            ),
            epsilon=0.0,
            lj_powers='12:6',
            mesh=dict(
                npx=0,
                npy=0,
                npz=0
            ),
            time_increment=dict(
                type='auto',
                auto=dict(
                    factor=0.0
                ),
                manual=dict(
                    delta_t=0.0
                )
            ),
            switch=dict(
                rotation='ON',
                lj_truncate='ON',
                init_distribution=dict(
                    type='uniform_random',
                    random_walk=dict(
                        iteration=0
                    ),
                    user_specify=dict(
                        particles=list(
                            [particle]
                        )
                    )
                ),
                init_orientation='use_specify',
                slip_tol=0.0,
                slip_iter=0,
                fix_cell=dict(
                    x='ON',
                    y='ON',
                    z='ON'
                ),
                pin=dict(
                    type='NO',
                    yes=dict(
                        pin=list(
                            [0]
                        ),
                        pin_rot=list(
                            [0]
                        )
                    )
                ),
                free_rigid=dict(
                    type='NO',
                    yes=dict(
                        dof=list(
                            [
                                dict(
                                    spec_id=0,
                                    vel=dict(
                                        x='NO',
                                        y='NO',
                                        z='NO'
                                    ),
                                    omega=dict(
                                        x='NO',
                                        y='NO',
                                        z='NO'
                                    )
                                )
                            ]
                        )
                    )
                ),
                ns_solver=dict(
                    obl_int='linear'
                )
            ),
            output=dict(
                gts=0,
                num_snap=0,
                avs='ON',
                on=dict(
                    out_dir='output',
                    out_name='data',
                    filetype='BINARY',
                    extended=dict(
                        driver=dict(
                            format='HDF5'
                        ),
                        print_field=dict(
                            crop='YES',
                            yes=dict(
                                slab_x=dict(
                                    x=0,
                                    y=0,
                                    z=0
                                ),
                                slab_y=dict(
                                    x=0,
                                    y=0,
                                    z=0
                                ),
                                slab_z=dict(
                                    x=0,
                                    y=0,
                                    z=0
                                )
                            ),
                            vel='YES',
                            phi='YES',
                            charge='YES',
                            pressure='YES',
                            tau='YES'
                        )
                    )
                ),
                udf='ON'
            ),
            resume=dict(
                calculation='NEW',
                continue_=dict(
                    saved_data=dict(
                        jikan=dict(
                            ts=0,
                            time=0.0
                        ),
                        particles=list(
                            [sparticle]
                        ),
                        gr_body=list(
                            [vector3d]
                        ),
                        gr_masses=list(
                            [0.0]
                        ),
                        gr_moments_body=list(
                            [matrix3d]
                        ),
                        zeta=list(
                            [[[
                                dict(
                                    zeta0=0.0,
                                    zeta1=0.0
                                )
                            ]]]
                        ),
                        uk_dc=vector3d,
                        concentration=list(
                            [[[[
                                dict(
                                    ck=0.0
                                )
                            ]]]]
                        ),
                        oblique=dict(
                            degree_oblique=0.0
                        )
                    )
                )
            )
        )
        self.params = None
        self.params_keys = [
            'constitutive_eq',
            'object_type',
            'a_xi',
            'a',
            'gravity',
            'epsilon',
            'lj_powers',
            'mesh',
            'time_increment',
            'switch',
            'output',
            'resume'
        ]

    def to_udf(self, filename='input.udf', path=None):
        """Make udf file.

        Parameters
        ----------
        filename: str or Path
            Filename to be made.
        Path: str, None or list of str
        """
        full_filename = find_file(filename, path)
        with full_filename.open(mode='w') as f:
            f.write('\\include{"define.udf"}\n')
            f.write('\\begin{data}\n')
            f.write(self.input_str())
            f.write('\n\\end{data}')

    def input_str(self):
        """Create string to write down into input file."""
        self.init_params()
        self._format_value(self.params)

        return self._udf_str(self.params)

    def load_pyconfig(self, filename='config.py', path=None):
        """Load confi file and update params.

        Parameters
        ----------
        filename: str or Path
            Filename to be loaded.
        Path: str, None or list of str
        """
        full_filename = find_file(filename, path)
        with full_filename.open(mode='rb') as f:
            exec(compile(f.read(), str(full_filename), 'exec'))

    def load_jsonconfig(self, filename='config.json', path=None):
        """Load confi file and update params.

        Parameters
        ----------
        filename: str or Path
            Filename to be loaded.
        Path: str, None or list of str
        """
        full_filename = find_file(filename, path)
        with full_filename.open(mode='rb') as f:
            config = json.load(f)
        deepupdate(self.data, config)

    def init_params(self):
        """Prepare dict whose keys are valid for gourmet."""
        params = dict()
        for key in self.params_keys:
            value = self.data[key]
            if key in ['a_xi', 'a', 'epsilon']:
                key = key.upper()
            elif key == 'lj_powers':
                key = 'LJ_powers'
            params[key] = value
        self.params = params

    def _udf_str(self, param_dict):
        """Create string valid for gourmet.

        Parameters
        ----------
        param_dict: dict
            Target dict to format. All values are list.

        Returns
        -------
        udf_str: str
            String valid for gourmet. This will be write down to udf file.

        Raises
        ------
        TypeError:
            If some param_dict's value are not list.
        """
        udf_str = ""
        indent = '    '
        indent_depth = 0

        lefts = ['{', '[']
        rights = ['}', ']']

        for key, values in param_dict.items():
            if not isinstance(values, list):
                raise TypeError(f"'{values}' is not list.")
            udf_str += f'{key}: '
            if len(values) >= 2:
                for i, value in enumerate(values):
                    udf_str += indent * indent_depth
                    udf_str += str(value)
                    if (i != (len(values) - 1)) \
                            and (value not in lefts) \
                            and (values[i + 1] not in rights):
                        udf_str += ','
                    if value in lefts:
                        indent_depth += 1
                    if (i != (len(values) - 1)) and (values[i + 1] in rights):
                        indent_depth -= 1
                    udf_str += '\n'
            else:
                values = values[0]
                udf_str += str(values)
                udf_str += '\n'

        return udf_str
