import pifacecad as pifacecad
cad = pifacecad.PiFaceCAD()

bitmaps = {}
bitmaps['PLAY'] = {'idx': 0, 'bitmap': pifacecad.LCDBitmap([0x10, 0x18, 0x1c, 0x1e, 0x1c, 0x18, 0x10, 0x0])}
bitmaps['PAUSE'] = {'idx': 1, 'bitmap': pifacecad.LCDBitmap([0x0, 0x1b, 0x1b, 0x1b, 0x1b, 0x1b, 0x0, 0x0])}
bitmaps['STOP'] = {'idx': 2, 'bitmap': pifacecad.LCDBitmap([0x0, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x0, 0x0])}
bitmaps['ERROR'] = {'idx': 3, 'bitmap': pifacecad.LCDBitmap([0x0, 0x1b, 0xe, 0x4, 0xe, 0x1b, 0x0, 0x0])}

cad.lcd.store_custom_bitmap(bitmaps['PLAY']['idx'], bitmaps['PLAY']['bitmap'])
cad.lcd.store_custom_bitmap(bitmaps['PAUSE']['idx'], bitmaps['PAUSE']['bitmap'])
cad.lcd.store_custom_bitmap(bitmaps['STOP']['idx'], bitmaps['STOP']['bitmap'])
cad.lcd.store_custom_bitmap(bitmaps['ERROR']['idx'], bitmaps['ERROR']['bitmap'])
