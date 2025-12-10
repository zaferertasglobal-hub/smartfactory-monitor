FROM amazoncorretto:21-alpine

WORKDIR /app

COPY . .

# BU SATIRLAR %100 ÇALIŞIR – Spring Boot 3+ için özel format
ENV SPRING_AUTOCONFIGURE_EXCLUDE=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration\
,org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration\
,org.springframework.boot.autoconfigure.sql.init.SqlInitializationAutoConfiguration

ENV MANAGEMENT_ENDPOINTS_WEB_EXPOSURE_INCLUDE=health

RUN ./mvnw clean package -DskipTests

EXPOSE 8080

# BU SATIRI EKLE – en garanti yöntem!
CMD ["java", "-Dspring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration,org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration", "-jar", "target/backend-java-0.0.1-SNAPSHOT.jar"]