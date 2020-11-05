import cModule
testVal = 12345
print ('success' if cModule.call_int(testVal)==testVal else 'failure')
