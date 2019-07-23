# Android build via Gradle
## Plugin version & Gradle version
https://developer.android.com/studio/releases/gradle-plugin

## Build
`./gradlew assembleDebug`
`./gradlew assembleRelease`
`./gradlew installDebug`
`./gradlew installRelease`
## 关键Task
assemble
build
check
clean
assemble= assembleDebug+assembleRelease
## 多渠道
productFlavors+manifest
`./gradlew assembleWandoujia`
`./gradlew assembleWandoujiaRelease`