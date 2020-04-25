import numpy as np

def get_flux_noise(device, omega, delta):
    # Return the deviation of frequency due to gaussian noise in flux
    # omega is the target frequency, delta is the std dev.
    Ejs = device.ejs
    Ejl = device.ejl
    Ec = device.ec
    gamma1 = Ejl/Ejs
    d1 = (gamma1 - 1)/(gamma1 + 1)
    flux_est = np.arccos((omega-3.75)/1.25)/(2*np.pi)
    flux_new = flux_est + np.random.normal(0,delta)
    def _Em(phi, m):
        # Asymmetric transmon
        return -(Ejs + Ejl)/2 + np.sqrt(4*(Ejs + Ejl)*Ec*np.sqrt(np.cos(np.pi*phi)**2 + d1**2*np.sin(np.pi*phi)**2))*(m + 1/2) - Ec*(6*m**2 + 6*m + 3)/12
    omega_old = _Em(flux_est, 1) - _Em(flux_est, 0)
    omega_new = _Em(flux_new, 1) - _Em(flux_new, 0)
    if omega_new > 5.0:
        omega_new = 5.0
    elif omega_new < 2.5:
        omega_new = 2.5
    return omega_new - omega_old


