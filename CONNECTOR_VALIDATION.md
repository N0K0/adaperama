# Connector Validation Report

Based on the TI HTML table provided, here's the validation status for all connectors:

## ✅ VALIDATED CORRECT

### TI 14-Pin (2.54mm)
All pins match the HTML table:
- Pin 1: TMS ✓
- Pin 7: TDO ✓
- Pin 13: EMU0 ✓
- Pin 14: EMU1 ✓
- All GND and KEY pins correct ✓

### ARM 14-Pin Legacy (OBSOLETE)
**CORRECTED** - Now matches HTML table:
- Pin 11: TDO (was incorrectly RTCK) ✓
- Pin 12: SRST (was nRESET) ✓
- Pin 2: GND (was Vsupply) ✓
- Missing RTCK (correct limitation) ✓

### TI 20-Pin Legacy (OBSOLETE)
All pins match the HTML table:
- Dual VTref on pins 1 & 2 ✓
- Pin 6: KEY ✓
- Pin 13: TDO ✓
- No EMU pins (correct) ✓

### Compact TI 20-Pin (cTI) - ✅ CORRECTED
**CORRECTED** - Now matches HTML table exactly:
- Pin 1: SWDIO/TMS (bidirectional) ✓
- Pin 2: nTRST ✓
- Pin 3: TDI ✓
- Pin 4: TDIS ✓
- Pin 5: VTref ✓
- Pin 6: KEY (mechanical keying) ✓
- Pin 7: SWO/TDO ✓
- Pin 11: SWCLK/TCK ✓
- Pin 15: nRESET ✓
- Pin 18: EMU3 (not GND) ✓
- Pin 19: EMU4 (not EMU3) ✓
- Supports both SWD and JTAG modes ✓
- Pin pitch 1.27mm, row pitch 2.54mm ✓

## ⚠️ NEEDS VALIDATION

### ARM 20-Pin (2.54mm)
Need to verify:
- Pin 1: VTref ✓
- Pin 2: NC/VDD or VSupply?
- Pin 15: nRESET vs nSRST?

### ARM Cortex 10-Pin (1.27mm)
HTML table shows dual-function pins:
- Pin 2: SWDIO / TMS
- Pin 4: SWDCLK / TCK
- Pin 6: SWO / TDO

Current spec uses these dual names ✓

## RECOMMENDATIONS

1. **cTI Connector:** Clarify if this is the same as our TI-CTI-20-1.27mm or a different connector
2. **ARM 20-pin:** Verify pin 2 naming (NC/VDD vs VSupply)
3. Review all connectors to ensure dual-function naming is consistent (e.g., "SWDIO / TMS" vs just "TMS")
