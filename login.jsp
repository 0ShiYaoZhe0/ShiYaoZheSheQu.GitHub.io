<!DOCTYPE html>
<%@ page language="java" contentType="text/html; charset=gbk"pageEncoding="gbk"%>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme() + + "://"
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
					<a>食尧者社区的第一阶段，正在开发中。。。。。。</a>
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
			 	 <%=name %>已登录
			 	 <%
			 	 	}
			 	  %>
			 </div>
			 <div id="content">
			 	<form method="post" action="LoginServlet" align="center">
			 		用户名：<input type="text" name="name" value=""/>口令（食尧者社区主饶正宇给的人社口令）：<input type="password" name="passwd" value="" style="width:155px"/><br>
			 	<p>
			 		<input type="submit" value="登录" name="submit" />
			 		<input type="reset" value="登录" name="" />
	 		 	</form>
			 </div>
		</div>
	</div>
</body>
</html>