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
