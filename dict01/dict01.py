#!/usr/bin/env python3
def main():
    switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendpr':' cisco'}
    print( switch['hostname'])
    print( switch['ip'])
#    print( switch['lynx'])

    print( "First test - .get()" )
    print( switch.get('lynx'))

    print("Second  test - .get()")
    print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

    print("Third test - .get()")
    print( switch.get('version'))


    print("Fourth  test - .keys()")
    print( switch.keys())

    print("Fith test - .values()")
    print( switch.values())


    print( "Sixth test - .pop()" )
    switch.pop('version') # removes this key (and value) pair
    print( switch.keys() )   # notice the value of version is gone
    print( switch.values() ) # notice the value 1.2

    print( "Seventh test - ADD a new value" )
    switch['adminlogin'] = 'karl08'
    print( switch.keys() )
    print( switch.values() )

    print( "Eighth test - ADD a new value" )
    switch['password'] = 'qwerty'
    print( switch.keys() )
    print( switch.values() )
 



main()


