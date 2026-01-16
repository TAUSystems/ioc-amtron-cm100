from org.csstudio.display.builder.runtime.script import PVUtil

trigger_pv, preset_value_pv, current_setpoint_pv = pvs

if PVUtil.getInt(trigger_pv) == 1:
    # Reset trigger variable
    trigger_pv.write(0)
    # Set current
    current_setpoint_pv.write(PVUtil.getDouble(preset_value_pv))
