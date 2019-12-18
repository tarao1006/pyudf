"""
This module defines aliases for udf file.
"""

vector3d = dict(
    x=0.0,
    y=0.0,
    z=0.0
)

quaternion = dict(
    q0=0.0,
    q1=0.0,
    q2=0.0,
    q3=0.0
)

matrix3d = dict(
    xx=0.0,
    xy=0.0,
    xz=0.0,
    yx=0.0,
    yy=0.0,
    yz=0.0,
    zx=0.0,
    zy=0.0,
    zz=0.0
)

particle = dict(
    r=vector3d,
    v=vector3d,
    q=quaternion,
    omega=vector3d
)

sparticle = dict(
    r=vector3d,
    r_raw=vector3d,
    v=vector3d,
    v_old=vector3d,
    f_hydro=vector3d,
    f_hydro_previous=vector3d,
    f_hydro1=vector3d,
    f_slip=vector3d,
    f_slip_previous=vector3d,
    fr=vector3d,
    fr_previous=vector3d,
    omega=vector3d,
    omega_old=vector3d,
    torque_hydro=vector3d,
    torque_hydro_previous=vector3d,
    torque_hydro1=vector3d,
    torque_slip=vector3d,
    torque_slip_previous=vector3d,
    torque_r=vector3d,
    torque_r_previous=vector3d,
    q=quaternion,
    q_old=quaternion
)

particle_spec = dict(
    particle_number=0,
    mass_ratio=0.0,
    surface_charge=0.0,
    janus_axis='NONE',
    janus_propulsion='OFF',
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

chain_spec = dict(
    beads_number=0,
    chain_number=0,
    mass_ratio=0.0,
    surface_charge=0.0,
    janus_axis='NONE'
)

rigid_spec = dict(
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

dof = dict(
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
