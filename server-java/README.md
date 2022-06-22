# Run

First of all, it is needed to clean, compile and package the maven project

```
cd {PATH_REPOSITORY}/server-java
mvn clean compile
mvn package
```

Then you need to run the server

```
cd {PATH_REPOSITORY}/server-java
mvn exec:java
```