from org.csstudio.display.builder.runtime.script import PVUtil

trigger_pv, increment_pv, current_pv = pvs

if PVUtil.getInt(trigger_pv) == 1:
    # Reset trigger variable
    trigger_pv.write(0)
    # Decrement current
    current_pv.write(PVUtil.getDouble(current_pv) - PVUtil.getDouble(increment_pv))
