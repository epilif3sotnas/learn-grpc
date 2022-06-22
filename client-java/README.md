# Run

First of all, it is needed to clean, compile and package the maven project

```
cd {PATH_REPOSITORY}/client-java
mvn clean compile
mvn package
```

Then you need to run the client

```
cd {PATH_REPOSITORY}/client-java
mvn exec:java
```