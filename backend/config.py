from configparser import ConfigParser

def config(filename = 'database.ini', section = 'postgresql'):
  # Create a parser
  parser = ConfigParser()
  # Read config file
  parser.read(filename)

  db = {}
  if parser.has_section(section):
    params = parser.items(section)
    for param in params:
      db[param[0]] = param[1] # We want to sign each element inside database.ini inside the db dictionary
  
  else:
    raise Exception('Section {0} not found in the {1} file '.format(section,filename))
  
  return db

