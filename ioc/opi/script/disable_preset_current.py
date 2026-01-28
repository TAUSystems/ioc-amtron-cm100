## Script for Rule: Enabled if preset within limit

from org.csstudio.display.builder.runtime.script import PVUtil

current_limit_pv, preset_value_pv = pvs

try:
    current_limit = PVUtil.getDouble(current_limit_pv)
    preset_value = PVUtil.getDouble(preset_value_pv)

## Script Body
    if preset_value > current_limit:
        widget.setPropertyValue('enabled', False)
    else:
        widget.setPropertyValue('enabled', True)

except (Exception, lang.Exception) as e:
    widget.setPropertyValue('enabled', True)
    if not isinstance(e, PVUtil.PVHasNoValueException):
        raise e
