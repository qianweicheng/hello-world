#Helm
Kubernates 的包管理器
##Tiller 权限问题
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
##App Store
https://hub.kubeapps.com/

15:10:42	CREATE TABLE IF NOT EXISTS `ep`.`ep_group_resource` (   `id` INT NOT NULL AUTO_INCREMENT,   `group_id` INT NULL,   `resource_id` INT NULL,   `state` CHAR(1) NULL DEFAULT 0,   `create_date` DATETIME NULL,   `create_user` VARCHAR(255) NULL,   `update_user` DATETIME NULL,   `update_date` VARCHAR(255) NULL,   PRIMARY KEY (`id`),   INDEX `id_group_idx` (`group_id` ASC),   INDEX `id_resource_idx` (`resource_id` ASC),   CONSTRAINT `id_group`     FOREIGN KEY (`group_id`)     REFERENCES `ep`.`ep_group` (`id`)     ON DELETE NO ACTION     ON UPDATE NO ACTION,   CONSTRAINT `id_resource`     FOREIGN KEY (`resource_id`)     REFERENCES `ep`.`ep_resource` (`id`)     ON DELETE NO ACTION     ON UPDATE NO ACTION) ENGINE = InnoDB	Error Code: 1022. Can't write; duplicate key in table 'ep_group_resource'	0.025 sec
