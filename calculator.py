"""
Open Geo Calc - Core Geotechnical Calculation Modules
"""

def calculate_darcy_velocity(k_cm_s: float, hydraulic_gradient: float) -> float:
    """
    Calculates seepage velocity using Darcy's Law.
    v = k * i
    """
    return k_cm_s * hydraulic_gradient

def calculate_manning_velocity(n: float, hydraulic_radius: float, slope: float) -> float:
    """
    Calculates open channel flow velocity using Manning's Equation.
    V = (1/n) * (R^(2/3)) * (S^(1/2))
    """
    if n <= 0:
        raise ValueError("Manning's roughness coefficient must be greater than zero.")
    return (1.0 / n) * (hydraulic_radius ** (2.0 / 3.0)) * (slope ** 0.5)

if __name__ == "__main__":
    # Example validation
    v_seepage = calculate_darcy_velocity(0.05, 0.25)
    print(f"Calculated Seepage Velocity: {v_seepage} cm/s")
