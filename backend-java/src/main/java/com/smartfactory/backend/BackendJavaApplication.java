package com.smartfactory.backend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class BackendJavaApplication {
    public static void main(String[] args) {
        SpringApplication.run(BackendJavaApplication.class, args);
    }
}

@RestController
class HealthController {
    @GetMapping("/api/health")
    public String health() {
        return "{\"status\":\"UP\",\"service\":\"SmartFactory Java Backend + WebSocket Ready\",\"timestamp\":\"2025\"}";
    }
}