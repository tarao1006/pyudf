# Example of config.

self.constitutive_eq['type'] = 'Shear_Navier_Stokes'
self.constitutive_eq['shear_navier_stokes']['dx'] = 1.0
self.constitutive_eq['shear_navier_stokes']['rho'] = 1.0
self.constitutive_eq['shear_navier_stokes']['eta'] = 1.0
self.constitutive_eq['shear_navier_stokes']['kbt'] = 0.0
self.constitutive_eq['shear_navier_stokes']['alpha_v'] = 1.0
self.constitutive_eq['shear_navier_stokes']['alpha_o'] = 1.0
self.constitutive_eq['shear_navier_stokes']['external_field']['type'] = 'DC'
self.constitutive_eq['shear_navier_stokes']['external_field']['dc']['shear_rate'] = 0.0


self.object_type['type'] = 'spherical_particle'
self.object_type['spherical_particle']['particle_spec'][0]['particle_number'] = 1
self.object_type['spherical_particle']['particle_spec'][0]['mass_ratio'] = 1.0
self.object_type['spherical_particle']['particle_spec'][0]['surface_charge'] = 1.0
self.object_type['spherical_particle']['particle_spec'][0]['janus_axis'] = 'Y'
self.object_type['spherical_particle']['particle_spec'][0]['jauns_propulsion'] = 'SQUIRMER'
self.object_type['spherical_particle']['particle_spec'][0]['janus_force']['x'] = 0.0
self.object_type['spherical_particle']['particle_spec'][0]['janus_force']['y'] = 0.0
self.object_type['spherical_particle']['particle_spec'][0]['janus_force']['z'] = 0.0
self.object_type['spherical_particle']['particle_spec'][0]['janus_torque']['x'] = 0.0
self.object_type['spherical_particle']['particle_spec'][0]['janus_torque']['y'] = 0.0
self.object_type['spherical_particle']['particle_spec'][0]['janus_torque']['z'] = 0.0
self.object_type['spherical_particle']['particle_spec'][0]['janus_slip_vel'] = 0.1
self.object_type['spherical_particle']['particle_spec'][0]['janus_slip_mode'] = 0.5
self.object_type['spherical_particle']['particle_spec'][0]['janus_rotlet_c1'] = 0.0
self.object_type['spherical_particle']['particle_spec'][0]['janus_rotlet_dipolr_c2'] = 0.0

self.a_xi = 2.0
self.a = 5.0
self.gravity['g'] = 0.0
self.gravity['g_direction'] = '-Y'
self.lj_powers = '36:18'
self.mesh['npx'] = 6
self.mesh['npy'] = 7
self.mesh['npz'] = 6
self.time_increment['type'] = 'auto'
self.time_increment['auto']['factor'] = 1.0

self.switch['rotation'] = 'ON'
self.switch['lj_truncate'] = 'ON'
self.switch['init_distribution']['type'] = 'user_specify'
self.switch['init_distribution']['user_specify']['particles'][0]['r']['x'] = 32.0
self.switch['init_distribution']['user_specify']['particles'][0]['r']['y'] = 64.0
self.switch['init_distribution']['user_specify']['particles'][0]['r']['z'] = 32.0
self.switch['init_distribution']['user_specify']['particles'][0]['v']['x'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['v']['y'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['v']['z'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['q']['q0'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['q']['q1'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['q']['q2'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['q']['q3'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['omega']['x'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['omega']['y'] = 0.0
self.switch['init_distribution']['user_specify']['particles'][0]['omega']['z'] = 0.0
self.switch['init_orientation'] = 'user_specify'
self.switch['slip_tol'] = 0.01
self.switch['slip_iter'] = 4
self.switch['fix_cell']['x'] = 'ON'
self.switch['fix_cell']['y'] = 'ON'
self.switch['fix_cell']['z'] = 'OM'
self.switch['pin']['type'] = 'YES'
self.switch['pin']['yes']['pin'][0] = 0
self.switch['pin']['yes']['pin_rot'][0] = 0
self.switch['free_rigid']['type'] = 'NO'
self.switch['ns_solver']['obl_int'] = 'linear'

self.output['gts'] = 100
self.output['num_snap'] = 400
