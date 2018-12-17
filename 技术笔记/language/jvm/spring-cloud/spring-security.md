## 重写WebSecurityConfigurerAdapter的几个方法，还有实现UserDetailService的几个接口
#### Spring cloud Security主要的任务是为spring cloud 中的各个组件提供token的中继功能，zuul，feign，RestTemplate
EnableOAuth2Client<-EnableOAuth2Sso
## OAuth Client
#### org.springframework.boot:spring-starter-security
- org.springframework.boot:spring-boot-starter
- org.springframework:spring-aop
- org.springframework.security:spring-security-config
- org.springframework.security:spring-security-web
#### org.springframework.boot:spring-boot-starter-web
#### org.springframework.cloud:spring-cloud-starter-oauth2
#### org.springframework.cloud:spring-cloud-cloudfoundry-web


## OAuth Serever
#### spring-boot-starter-security
#### spring-security-oauth2
#### spring-security-jwt
#### spring-boot-starter-web


## org.springframework.cloud:spring-cloud-starter-security
- org.springframework.cloud:spring-cloud-starter
- org.springframework.cloud:spring-cloud-security
## org.springframework.security.oauth:spring-security-oauth2
- org.springframework.security:spring-security-core
- org.springframework.security:spring-security-config
- org.springframework.security:spring-security-jwt
- org.springframework.security:spring-security-web
## org.springframework.cloud:spring-cloud-starter-oauth2
- org.springframework.cloud:spring-cloud-starter-security
- org.springframework.security.oauth:spring-security-oauth2
- org.springframework.security:spring-security-jwt


#### OAuth2配置
BaseOAuth2ProtectedResourceDetails<-ClientCredentialsResourceDetails
EnableGlobalAuthentication<-EnableWebSecurity