<!DOCTYPE html>
<%@ page language="java" contentType="text/html; charset=gbk"pageEncoding="gbk"%>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme() + "://"
    	+ request.getServerName() + ":" + request.getServerPort()
    	+ path + "/";
%>
<html>
<head>
<meta http-equiv="Content-Type" Content="text/thml; charset=gbk">
<link href="css/layout.css"rel="stylesheet" type="text/css"/>
</head>
<body>
	<div id="container">
		<div id="header">
			<div align="center">
				<marquee>
					<a>ʳҢ�������ĵ�һ�׶Σ����ڿ����С�����������</a>
				</marquee>
			</div>
		</div>
		<div id="mainContent">
			<%
				String name = (String) session.getAttribute("name");
			 %>
			 <div id="sidebar">
			 	<%
			 		if (name == null){
			 			name = "";
			 		}else{
			 	 %>
			 	 <%=name %>�ѵ�¼
			 	 <%
			 	 	}
			 	  %>
			 </div>
			 <div id="content">
			 	<form method="post" action="LoginServlet" align="center">
			 		�û�����<input id="userName"type="text" name="name" value=""/>
			 		���ʳҢ�������������������������<input id="userPwd"type="password" name="passwd" value="" style="width:155px"/><br>
			 	<p>
			 <script language="javascript" type="text/javascript">
			 	function validate(){
			 		var userName = document.getElementById("userName").value;
			 		var userName = document.getElementById("userPwd").value;
			 		if (!(userName == "0ShiYaoZhe0" || userPwd =="11451419")){
			 			document.getElementById("login").submit();
			 		}else{
			 			alert("��¼��Ϣ����ȷ")
			 		}
			 	}		
			 </script>
			 		<input type="submit" value="��¼" name="submit" />
			 		<input type="reset" value="����" name="" />
	 		 	</form>
			 </div>
		</div>
	</div>
</body>
</html>