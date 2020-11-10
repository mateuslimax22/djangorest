# Vulnerability Manager

         A project in django rest framework to facilitate control of vulnerabilities in hosts.

## Installation
Clone repository
```bash
    git clone https://github.com/mateuslimax22/djangorest.git
```
Setup project environment with virtualenv.

```bash
    virtualenv project-env
    source project-env/bin/activate
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requiments.txt.

```bash
    pip install -r requirements.txt
```
## Get Started
### Database
```bash
    Configure your database, more informations:
 ```
        https://docs.djangoproject.com/pt-br/1.11/intro/tutorial02/
    
### Create tables::
```bash
    ./ python manage.py migrate
```
### Create a superuser::
```bash
   ./ python manage.py createsuperuser
```
## Usage
```bash
   python manager.py runserver
   Starting development server at http://localhost:8000/
```
## Load data
```bash
   python manager.py open_csv.py
```
## Routes
![img](https://i.imgur.com/zYBiaJ0.png)
```bash
   GET localhost/vulnerabilities/
   Returns all vulnerabilities
```
![img](https://i.imgur.com/wzmevT3.png)

```bash
   GET localhost/hosts/
   Returns all hosts
```
![img](https://i.imgur.com/7GersRo.png)

```bash
   GET localhost/hosts/id/list
   Details of a specific host
```
![img](https://i.imgur.com/ilsXy3M.png)

```bash
   GET localhost/vulnerabilities/id/list
   Details of a specific vulnerability
```
![img](https://i.imgur.com/40EGX9x.png)


```bash
   PUT localhost/vulnerabilities/id
   Update vulnerability fix key
```
![img](https://i.imgur.com/ahG6Po7.png)

## Filters
![img](https://i.imgur.com/lBPDMF1.png)

```bash
   Filter vulnerability to severity
   GET /vulnerabilities/?vulnerability_severity=M%C3%A9dio&host_list__asset_hostname=
```
```bash
   Filter vulnerability to hostname
   GET /vulnerabilities/?vulnerability_severity=&host_list__asset_hostname=WORKSTATION-1
   GET /vulnerabilities/?search=WORKSTATION-1
```
```bash
   Ordering vulnerability to title
   GET /vulnerabilities/?ordering=vulnerability_title
```
```bash
   Ordering vulnerability to severity
   GET /vulnerabilities/?ordering=vulnerability_severity
```
```bash
   Ordering vulnerability to cvss
   GET /vulnerabilities/?ordering=vulnerability_cvss
```
```bash
   Ordering vulnerability to fix key 
   GET /vulnerabilities/?ordering=vulnerability_fixed
```
```bash
   Ordering vulnerability to publication date
   GET /vulnerabilities/?ordering=vulnerability_publication_date
```
```bash
   Ordering vulnerability to publication date
   GET /vulnerabilities/?ordering=vulnerability_publication_date
```
![img](https://i.imgur.com/7HWvmJs.png)

```bash
   Filter host to vulnerability
   GET /hosts/?host__vulnerability_title=VMware+ESXi+5.5+%2F+6.0+%2F+6.5+%2F+6.7+DoS+%28VMSA-2018-0018%29+%28remote+check%29
   GET /hosts/?search=VMware+ESXi+5.5+%2F+6.0+%2F+6.5+%2F+6.7+DoS+%28VMSA-2018-0018%29+%28remote+check%29
```
```bash
   Ordering host to name
   GET /hosts/?ordering=asset_hostname
```
```bash
   Ordering host to number vulnerability
   GET /hosts/?ordering=num_vulnerability
```
## Authentication
![img](https://i.imgur.com/quL31lO.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
