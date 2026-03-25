"""Registry platforem pro školení."""

from platforms.civop import CivopPlatform
from platforms.lrn import LrnPlatform
from platforms.cisco import CiscoBlackBeltPlatform

PLATFORMS = {
    "civop": CivopPlatform,
    "lrn": LrnPlatform,
    "cisco": CiscoBlackBeltPlatform,
}
