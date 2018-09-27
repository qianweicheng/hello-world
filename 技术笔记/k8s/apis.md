https://api.stag.easilydo.cc/api/v1/namespaces/default/pods
https://api.stag.easilydo.cc/apis/apps/v1/deployments
https://api.stag.easilydo.cc/apis/apps/v1/namespaces/default/deployments
https://api.stag.easilydo.cc/apis/extensions/v1beta1/deployments （废弃）

https://api.stag.easilydo.cc/apis/apps/v1/namespaces/default/statefulsets

kubectl patch deployment busybox --patch "$(cat tmp.yaml)"