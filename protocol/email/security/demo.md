# 邮件代发
邮件代发服务发送到各个邮件服务商之后各自会添加自己的一些Header进去
## neteasy
```
Received: from a27-38.smtp-out.us-west-2.amazonses.com (unknown [54.240.27.38])
	by mx19 (Coremail) with SMTP id x8mowAAX4tcS6zReRf_REg--.49102S3;
	Sat, 01 Feb 2020 11:05:57 +0800 (CST)
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=gdwg2y3kokkkj5a55z2ilkup5wp5hhxx; d=amazonses.com; t=1580526353;
	h=From:To:Subject:MIME-Version:Content-Type:Content-Transfer-Encoding:Message-ID:Date:Feedback-ID;
	bh=CdyLZkJ8lmcG6LGqQLJ9wGHjTGm+KnpUC9dYcise+EQ=;
	b=hrSTgXUzKneh8OhdXKkSBMZ3sPsDGKQVoxU+UzSrRsz09k9991T0RGiWaXfvxNYC
	+rjOQWKeXMAtMqsxoMuzsuiGNoerv/ErqcfidCmWkn+w78yCsaf4VcN9kW+q1lo4afn
	bQtWCbfnGww5c71pEseQtP+cDlwKNJv9ApDjAaOc=
From: qweiczhong@gmail.com
To: edotest1@126.com
Subject: Send From AWS
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 7bit
Message-ID: <0101016ffeb63bb7-a63b8f9e-44d0-4b12-bbb1-01b2b11f319d-000000@us-west-2.amazonses.com>
Date: Sat, 1 Feb 2020 03:05:53 +0000
X-SES-Outgoing: 2020.02.01-54.240.27.38
Feedback-ID: 1.us-west-2.SK64Hb0iaJU5P6aN2hzel1nsxy4lpETy5H8O0BCHUTo=:AmazonSES
X-CM-TRANSID:x8mowAAX4tcS6zReRf_REg--.49102S3
Authentication-Results: mx19; spf=pass smtp.mail=0101016ffeb63bb7-a63b
	8f9e-44d0-4b12-bbb1-01b2b11f319d-000000@us-west-2.amazonses.com; dkim=
	pass header.i=@amazonses.com
X-Coremail-Antispam: 1Uf129KBjDUn29KB7ZKAUJUUUUU529EdanIXcx71UUUUU7v73
	VFW2AGmfu7bjvjm3AaLaJ3UbIYCTnIWIevJa73UjIFyTuYvjxUh8sqDUUUU
Sender: 0101016ffeb63bb7-a63b8f9e-44d0-4b12-bbb1-01b2b11f319d-000000@us-west-2.amazonses.com
```
## Gmail
```
Delivered-To: weicheng@edison.tech
Received: by 2002:a0c:c44a:0:0:0:0:0 with SMTP id t10csp190775qvi;
        Fri, 31 Jan 2020 19:11:49 -0800 (PST)
X-Google-Smtp-Source: APXvYqwpuxPM322to/JeB9vdyEiFI32grgF4VS0aBb2tnz8O66bBUgAb2uqjGwXxsUIQ1WeXqaWV
X-Received: by 2002:aa7:90c5:: with SMTP id k5mr13791296pfk.143.1580526709246;
        Fri, 31 Jan 2020 19:11:49 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1580526709; cv=none;
        d=google.com; s=arc-20160816;
        b=t1JPtaxaaoFSiwEcqgKQt3YJDzGtvgZIB0kj3F3JX8odNJgT7dJb3dZDQ1et4E8WYO
         TvoTBKkYgmUr/0MiKwXDijyDspjw3GOSkIGAcQadZ1Ikuavx94XaEaynrxji3SAh0F0f
         d4ciJUdYOE1Kffsf/gkq1neTa1Zq3T6nbZJRQoQmGKJGNzYHWn6hre4Oq8avB4QQCaA4
         5SihnAamU2iVOvThxw8b09sBeOHgEY1KQCxR55E/cfHOCVVwOymhnU+U3Ws5s294YR7j
         fc265YOzoKdqvbXcE02TIGTSO27tUKrbx7cxrtgZEgSCYquMuWjGgp/EF0UgKpxcSFJL
         n3uA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:date:message-id:content-transfer-encoding:mime-version
         :subject:to:from:dkim-signature;
        bh=WN9jjFu//8qtE8luk5bNJWZe8eu6jn90bWUEPF3q5DU=;
        b=QEBXHVZGpq/RnJNpLtlggA8qui/71MfLIMY9Hk+LDWyO+Zm7Nbb0DK4EssMQ2brc42
         sgTStE2Jn9HaAiE63ZoDq74PSYZT+IvYpdbqHQA6OmWlqmACBLa9lbQXeuuTQotDi2sn
         9p6VaNSR1Q1RucyJljAO7f4yVoaeHonI7XeHy0qpVgxq//TJIEnEECQSk8Ka0T6FSuq4
         P6knRu0KPBQdBlwZe5kOjDvzZFb9m3MHQQkNTgb7xWpHOPiEEtED0A4hMKdYsSdNfRsX
         SWR0zUp5YvaPVP5mSDHfxmLN9gOYYFob3581EZ1S/CKINmUposfdJz0e2CmwCRJeOmZU
         330w==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@amazonses.com header.s=gdwg2y3kokkkj5a55z2ilkup5wp5hhxx header.b=FxxfSHRK;
       spf=pass (google.com: domain of 0101016ffebba6b4-f270fd02-a80c-45bd-bf0b-419507e4e741-000000@us-west-2.amazonses.com designates 54.240.27.116 as permitted sender) smtp.mailfrom=0101016ffebba6b4-f270fd02-a80c-45bd-bf0b-419507e4e741-000000@us-west-2.amazonses.com;
       dmarc=fail (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
Return-Path: <0101016ffebba6b4-f270fd02-a80c-45bd-bf0b-419507e4e741-000000@us-west-2.amazonses.com>
Received: from a27-116.smtp-out.us-west-2.amazonses.com (a27-116.smtp-out.us-west-2.amazonses.com. [54.240.27.116])
        by mx.google.com with ESMTPS id s8si1925252pji.72.2020.01.31.19.11.48
        for <weicheng@edison.tech>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-SHA bits=128/128);
        Fri, 31 Jan 2020 19:11:49 -0800 (PST)
Received-SPF: pass (google.com: domain of 0101016ffebba6b4-f270fd02-a80c-45bd-bf0b-419507e4e741-000000@us-west-2.amazonses.com designates 54.240.27.116 as permitted sender) client-ip=54.240.27.116;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@amazonses.com header.s=gdwg2y3kokkkj5a55z2ilkup5wp5hhxx header.b=FxxfSHRK;
       spf=pass (google.com: domain of 0101016ffebba6b4-f270fd02-a80c-45bd-bf0b-419507e4e741-000000@us-west-2.amazonses.com designates 54.240.27.116 as permitted sender) smtp.mailfrom=0101016ffebba6b4-f270fd02-a80c-45bd-bf0b-419507e4e741-000000@us-west-2.amazonses.com;
       dmarc=fail (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple; s=gdwg2y3kokkkj5a55z2ilkup5wp5hhxx; d=amazonses.com; t=1580526708; h=From:To:Subject:MIME-Version:Content-Type:Content-Transfer-Encoding:Message-ID:Date:Feedback-ID; bh=WN9jjFu//8qtE8luk5bNJWZe8eu6jn90bWUEPF3q5DU=; b=FxxfSHRKNP62BmShwsf1GGhkuyYfCMXKXUzVk1Y20K1c3gcTT38WyWLFmry7MQG0 0XHmsEQOZFwtwzX03JwITbCbIGbcjG1ec7HXTEFqag2rOQ0t9DvY4XG61IcK+suL/A5 GEvrwRcpLR8UUyXiE+9SPVWBVnuDuSGpeEQuQ/cw=
```
## QQ
```
Received: from 54.240.27.38 (unknown [54.240.27.38])
	by newmx40.qq.com (NewMx) with SMTP id 
	for <qweic@qq.com>; Sat, 01 Feb 2020 11:20:03 +0800
X-QQ-FEAT: HirWekLIAYLcThpN4oNGG+oo1b3YQgVzGYRi30QIzjmKUquJfKRc1xzXv1JS+
	/mOuL1ZCfk+46H7w4EVfKlCBRSda4ZZiEZ6WzJar2T1cegLwlb04Qr2N+nLU8FvCSGl1DH6
	+rRAnaCJU5+z2b9Z6VXim9kQg8v2hwxt3foPvBNBrx64tmxEe8OW+5+Fg8FMgM8vr7N0WtX
	nhzTw+lb9QdbvGmLDFGH0eZZEq8m/Zz4tpaS4RxMK/ZCrlx6iHG81In9lpbucRJd0vgjVYw
	r0chnKMP2Jm3jd
X-QQ-MAILINFO: M9mpTqh4QKvqvTd8wTE1X7z1d9KQoj+vz2a8rwRPwJ8gLBl8BQBPtb0Fz
	FPTbsawx1iB3PwaIZyjh/ylnIuD7M9wNvGRuSeMhjjol2dSzdGyYLTrMX+6Sx2BeS5DMiN9
	AxiBCYZ5Hz/jLn0o8OkfoEPhXG4dJOcnBPky00DQiJtgnk68kYuKBns=
X-QQ-mid: mxszc19t1580527179t7of1hq7a
X-QQ-CSender: us-west-2.amazonses.com#qweiczhong@gmail.com
X-QQ-ORGSender: 0101016ffec32e1d-d226aca5-f935-4e61-a598-c40957dc1ddc-000000@us-west-2.amazonses.com
X-QQ-XMAILINFO: OJ2W/SAh+iwCQnhguaFfgzTE2wjjGyK3ebAyzz/9rKnWwLyIQqWLLo5uQqKieZ
	 q2NV3urR91jiaW5Kol9UmLRWTfcohSu9/IYUhcF/gI9LIEFuE8pzlftdGljySV1A8XQAALANyJ0U
	 qgkDyX9owGZmAMUeGhIvw8nqKMoQy20x5Ed7j0SkgqjjgbYKD+j9jawMMAJi1i/KUaLJUswAypB8
	 aNytz4pxWVk7F6N74tcoakChc0yN/cPzcokwVOOXxVUQeIsaXE38z6KxHvWNw9TLYjib3DcafzVr
	 kw1hqj9PD2LnpgzNOFEPI/miWSK4hwOrbIEHTcruHqguVSysM7jtdX/ouC40hv/6n3zRthEL15hb
	 Pvt2NgErMOIz+g4OKfhYcnjJkU3gk93PCraCXjgHx6JPibmAMXz5x6DcTS6GbwMYXxIy60qPYrlX
	 UjK4IPHm5sWeCu1XKxHwQPpbHsq/ueAA9nT1NIf9WQXAqsDL/pyC2PaMroDt4adIVECgzMd2j7Hp
	 4z/o+sRVFjyC8X4p7eUKlOhEDTCGVl7RTGWhuNYTEUdjAE63NPu+HAGfU4OvVhHpDT4e4fXFS97M
	 A1uyrg7bpCDAKC6phf9UH9CgOFRqOi4QL7ZGFNrI1eSra3bn2SxXrNC9xRRg+eaVic5myM+98FZY
	 k/mAObL7FsvegvWcQn5jkL22lTP+Euco/icS8qOf8UsXuTcJdsz5HTAeJQH9JitbiQkTJAB3kj7o
	 rcC4+CWU9GRxM=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=gdwg2y3kokkkj5a55z2ilkup5wp5hhxx; d=amazonses.com; t=1580527202;
	h=From:To:Subject:MIME-Version:Content-Type:Content-Transfer-Encoding:Message-ID:Date:Feedback-ID;
	bh=WN9jjFu//8qtE8luk5bNJWZe8eu6jn90bWUEPF3q5DU=;
	b=FwLR1xrl/lLkvIuzcA7nrEhNXdVq1cFW339yXRXX7qx4Iyt4upBXa0tyebVfHsUG
	MMe1n45uSgDQMRUkMfvkK/oLMtEo4l0g0jmCovC+Kj+W3tFx8YmH70yZx+GHN0igHNl
	/mVJyyMPUV3bfjbrVvmBUW8mK/MhRN/WGrDQmgN0=
```
## 结论
- QQ: 使用X-QQ-CSender和X-QQ-ORGSender
- Neteasy: 使用Sender
- Gmail:
