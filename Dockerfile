FROM eclipse-temurin:23.0.1_11-jre-alpine
WORKDIR /app
RUN apk add dumb-init
COPY ./target/spring-petclinic-4.0.1-SNAPSHOT.jar /app/spring-petclinic-4.0.1-SNAPSHOT.jar
RUN addgroup --system petclinic && adduser petclinic -S -s /bin/false -G petclinic petclinic
RUN chown -R petclinic:petclinic /app
USER petclinic
EXPOSE 8080
ENTRYPOINT ["dumb-init", "java", "-jar", "spring-petclinic-4.0.1-SNAPSHOT.jar"]
