# MICROSERVICE TEMPLATES

## GUIDING PRINCIPLES

**MICROSERVICE SINGLE RESPONSIBILITY**
- a microservice should only be responsible in doing only one domain

**Single Source of Truth**
- Every piece of information in a microservice should be managed authoritatively by a single service 

**Implementation Cost** 
- What the project/organization's budget 

## API GATEWAY IMPLEMENTATION
![gateway](./docs/microservice-api-gateway.png)

## Authentication Frameworks

**SuperTokens**
```
npx create-supertokens-app@latest
```
https://supertokens.com/

## TO FOLLOW

Add validations for security
```python
import re

def filter_payloads(string):
    xss_pattern = re.compile(r'<|>|javascript:|on\w+\s*=|alert\(|script\s*>', re.IGNORECASE)
    sql_pattern = re.compile(r'SELECT|UPDATE|DELETE|INSERT|DROP|--|#', re.IGNORECASE)
    filtered_string = re.sub(xss_pattern, '', string)
    filtered_string = re.sub(sql_pattern, '', filtered_string)
    return filtered_string

```


## REFERENCES

- Authentication & Authorization in Microservice Architectures
> https://www.youtube.com/watch?v=AQ-JMjPoPIc
