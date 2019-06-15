import inquirer
import os
import click
import constants
import re
questions = [
    inquirer.List(constants.CLIENT,
                  message="What is your kind of database",
                  choices=[
                      ('Mongo', constants.MONGO),
                      ('Postgres', constants.POSTGRESS),
                      ('Mysql', constants.MYSQL)
                  ],
                  ),
    inquirer.Text(constants.NAME, message="Name"),
    inquirer.Text(constants.HOST, message="Host"),
    inquirer.Text(constants.PORT, message="Port"),
    inquirer.Text(constants.USERNAME, message="Username"),
    inquirer.Text(constants.PASSWORD, message="Password"),
    inquirer.Text(constants.PATH, message="PATH"),
    inquirer.Text(constants.DEPENDENCES, message="dependences")
    # inquirer.Path(constants.PATH,
    #               message="Path your project strapi",
    #               path_type=inquirer.Path.DIRECTORY,
    #               )
]
answers = inquirer.prompt(questions)

click.echo('Installing strapi lastest version Beta 😋 ️')

client = answers[constants.CLIENT]
dependences = re.split(r'\s*,\s*', answers[constants.DEPENDENCES])
#path = answers[constants.PATH]
path = (answers[constants.PATH],
        "/home/gianca/devpower/apicocanasa/")[not answers[constants.PATH]]
name = (answers[constants.NAME], "test1")[not answers[constants.NAME]]
username = (answers[constants.USERNAME], " ")[not answers[constants.USERNAME]]
password = (answers[constants.PASSWORD], " ")[not answers[constants.PASSWORD]]
port = (answers[constants.PORT], "27017")[not answers[constants.PORT]]
host = (answers[constants.HOST], "127.0.0.1")[not answers[constants.HOST]]

create_project_strapi = constants.CREATE_PROJECT + name + constants.DB_CLIENT + client +\
    constants.DB_HOST + host + constants.DB_PORT + port+constants.DB_NAME + name +\
    constants.DB_USERNAME + username + constants.DB_PASSWORD + password
print(create_project_strapi)
deleteAdmin = constants.RM_R+path+constants.ADMIN
existExtension = os.path.exists(
    path+constants.PATH_EXTENSIONS_PERMISSION_CONFIG)

if(not existExtension):
    createExtension = constants.MKDIR_P+path + \
        constants.PATH_EXTENSIONS_PERMISSION_CONFIG
    os.system(createExtension)
    cpJWT = constants.CP+path+constants.PATH_JWT+" " + \
        path+constants.PATH_EXTENSIONS_PERMISSION_CONFIG
    os.system(cpJWT)

deletePlugins = constants.RM_R+path+constants.PLUGINS
deleteServerjs = constants.RM+path+constants.SERVER_JS
cpPackageJson = constants.CP+name+constants.PACKAGE_JSON+" "+path
rmNodeModule = constants.RM_R+path+constants.NODE_MODULES
installNodeModule = constants.CD+path+"&&"+constants.INSTALL
deletePackageLock = constants.RM+path+constants.PACKAGE_LOCK
pathGitIgnore = path+constants.GITIGNORE
print (pathGitIgnore)
fileGitIgnore = open(pathGitIgnore,"a")
fileGitIgnore.writelines("############################ \n # Strapi \n ############################ \nexports+\n"
                    ".cache \n build \n")
fileGitIgnore.close()
print(fileGitIgnore)
# os.system(constants.INSTALL_STRAPI)
print(create_project_strapi)
# os.system(create_project_strapi)
# os.system(deleteAdmin)
# os.system(deletePlugins)
# os.system(deleteServerjs)
# os.system(cpPackageJson)
# os.system(rmNodeModule)
# os.system(deletePackageLock)
# os.system(installNodeModule)
click.echo('Installing node ️')
for dependece in dependences:
    installDependence = constants.CD+path+"&&"+constants.INSTALL_SAVE+dependece
    # os.system(installDependence)

print(answers)
