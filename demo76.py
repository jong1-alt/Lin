def variable_key_value_function(fix, **kwargs):
    print(f'fix part={fix}')
    for k, v in kwargs.items():
        print(f"parameter name={k}, value={v}")


variable_key_value_function("parameter alone")
variable_key_value_function('POOP',name='python programming' )
variable_key_value_function('POOP',name='python programming',
                            duration=35,level='beginning')
course = {'code':'POOP',
          'name':'Python programming',
          'duration':35,
          'level':'beginning',
          'seasion':'winter'}
variable_key_value_function('POOP',**course)