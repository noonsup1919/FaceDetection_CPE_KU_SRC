er = int(input('input bit:'))

eg = float(input('input Vcc:'))

et = float(input('input Vin:'))

raw = int((2**er)-1)

raw = int(raw/eg)

raw = raw = int(raw*et)

data = raw * eg
data = data /((2**er)-1)

err = abs(data-et)
err = err/et
err = err * 100
print("Output RAW :"+str(raw))
print("Output DATA: ","%.4f"%data,end = '')
print(" error ""%.4f"%err,end = ' %')
