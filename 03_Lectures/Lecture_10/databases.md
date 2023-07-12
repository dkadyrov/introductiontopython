# Databases
## 2 Types of Databases
### Structured

Example Driver's License Database
- name
- date of birth
- address
- drivers id
- eye color
- height
- picture 

Example Police Database
- name 
- drivers id -> Driver's License Database 
    - address
    - eye color
    - height
- criminal history

Example IRS Database
- name
- social security number 
- taxes

Example Bank
- name
- social security number
- credit score

Industry: 
    SQL 
    - mySQL (server) <- Oracle
    - SQLite (file)
    - PostGreSQL (server)


### Relationships

One-to-One Relationship
- Social Security number
- Drivers License number
- Email address
- Amazon order number

One-to-Many Relationship
- Date of Birth
- Address
- One Child, 2 parents
- One parent, multiple children

Many-to-Many Relationship
- Amazon products  


## Unstructured 

Slower

Industry: 
    MongoDB 

Spotify: 
- mutiple artists on one track
- artists multiple different songs, remixes, 
- songs might have lyrics
- 