# To Do


## Development

### Models
- [x] `Work` model
  - declared fields: `work_title`, `work_summary`, `date_created`
- [x] `WorkPart` model
  - declared fields: `related_work`, `work_part_text`
- [ ] create migration 
- [ ] add test data via api and frontend
  - [ ] dump app-specific test data
  - [ ] abstract more test data using .json dump?


### Tests and testing
- [ ] start test idea log you to extrapolate from



## Initializing the repo

### Text and documentation
- [x] add `TODO.md`
- [ ] fill out `README.md` with:
  - [ ] details about what we're planning to do
  - [ ] links to important info
- [ ] get the wiki started with:
  - [x] the 0.1.0 spec
  - [ ] barebones installation instructions for people wanting to run/test the software
    - [x] on windows
    - [ ] on mac

### Test stack
- [x] add and configure Django 2.0 barebones install
  - [x] default install files
  - [x] default install db
  - [x] default site settings
  - [x] initial db migration files
    - [x] default model migration file
    - [x] data fixture to plug into default models 
- [x] initialize FanArchive app in Django
- [x] set Jinja2 as templating engine
  - [x] install django_jinja to make it go
  - [x] change settings.py accordingly

### Branch setup
- [x] development branch
