<?php
   if (isset($_POST["submit"])) {
   $name = $_POST['name'];
   $email = $_POST['email'];
   $message = $_POST['message'];
   $from = 'Notas de aula';
   $to = 'phkonzen@gmail.com'; 
   $fromurl = $_POST["from_url"];
   $subject .= '[Notas] ' . $fromurl;

   $message = wordwrap($message, 70, "\r\n");

   $ip = $_SERVER['REMOTE_ADDR'];

   $body ="De: $name\nE-mail: $email\nIP: $ip\n\nRef. a URL: $fromurl\n\nMensagem:\n $message";

   //Check if message has been entered
   if (!$_POST['message']) {
   $errMessage .= "Por favor, digite sua mensagem. ";
   }

   // If there are no errors, send the email
   if (!$errMessage) {
   if (mail ($to, $subject, $body, $from)) {
   $result = '<div class="alert alert-success">Obrigado por sua mensagem!</div>';
   } else {
   $result ='<div class="alert alert-danger">Desculpe, houve um erro ao enviar sua mensagem. Caso o problema persista, considere entrar em contato pelo e-mail: <a href="mailto:phkonzen@gmail.com" target="_top">phkonzen@gmail.com</a>.</div>';
   }
   ?>

<!DOCTYPE html>
<html lang="pt">
  <head>
    
    <meta charset="utf-8">
    <meta name="Description"
	  CONTENT="Notas de aula,
		   Pedro H A Konzen.">
    <meta name="keywords" content="notas de aula,
				   matemática,
                                   mensagem de usuário">
    <title>Mensagem de usuário</title>
    <meta name="author" content="Pedro H A Konzen">
    <link href='http://fonts.googleapis.com/css?family=Open Sans:400,700'
	  rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="index.css" type="text/css">

    
  </head>

  <body>
    <?php $fromurl0 = $_SERVER['HTTP_REFERER']; ?>

    <div class="row">
      <div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-2">
	
	<!-- begin: navbar -->
	
	<nav class="navbar navbar-default">
	  <div class="container-fluid">
	    <div class="navbar-header">
	      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
		<span class="sr-only">Toggle navigation</span>
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>
	      </button>
	      <a class="navbar-brand" href="main.html">Notas de Aula</a>
	    </div>

	    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
	      <ul class="nav navbar-nav">
		<li><a href="https://github.com/phkonzen/notas">Repositório GitHub</a></li>
		<li><a href="../index.html">Notas & Infos</a></li>
	      </ul>
	    </div><!-- /.navbar-collapse -->
	  </div><!-- /.container-fluid -->
	</nav>
	
	<!-- end: navbar -->
	
	<div class="titulo">
	  <div class="container-fluid">
  	    <h2 class="text-center" style="margin-bottom:0px;"> Mensagem de usuário</h2>
	  </div>
	</div>

	<form class="form-horizontal" role="form" method="post" action="contato.php">
	  <div class="form-group">
	    <label for="name" class="col-sm-2 control-label">Nome</label>
	    <div class="col-sm-10">
	      <input type="text" class="form-control" id="name" name="name" placeholder="(opcional)" value="<?php echo htmlspecialchars($_POST['name']); ?>">
	    </div>
	  </div>
	  <div class="form-group">
	    <label for="email" class="col-sm-2 control-label">E-mail</label>
	    <div class="col-sm-10">
	      <input type="email" class="form-control" id="email" name="email" placeholder="(opcional)" value="<?php echo htmlspecialchars($_POST['email']); ?>">
	    </div>
	  </div>
	  <div class="form-group">
	    <label for="from_url" class="col-sm-2 control-label">Ref. à página</label>
	    <div class="col-sm-10">
	      <input type="text" class="form-control" id="from_url" name="from_url" placeholder="<?php if (isset($_SERVER['HTTP_REFERER'])) { echo htmlspecialchars($_SERVER['HTTP_REFERER']);} else {echo 'Informe o link da página referente ao seu aviso';} ?>" value="<?php echo htmlspecialchars($_SERVER['HTTP_REFERER']); ?>">
	    </div>
	  </div>
	  <div class="form-group">
	    <label for="message" class="col-sm-2 control-label">Mensagem</label>
	    <div class="col-sm-10">
	      <textarea class="form-control" rows="4" name="message" placeholder="Digite seu aviso de erro ou sugestão aqui."><?php echo htmlspecialchars($_POST['message']);?></textarea>
	      <?php echo "<p class='text-danger'>$errMessage</p>";?>
	    </div>
	  </div>
	  <div class="form-group">
	    <div class="col-sm-10 col-sm-offset-2">
	      <input id="submit" name="submit" type="submit" value="Enviar" class="btn btn-primary">
	    </div>
	  </div>
	  <div class="form-group">
	    <div class="col-sm-10 col-sm-offset-2">
	      <?php echo $result; ?>	
	    </div>
	  </div>
	</form> 

<div class="panel panel-default">
<div class="panel-body" style="text-align: right">
Repositório GitHub: <a href="https://github.com/phkonzen/notas" target="_blank">https://github.com/phkonzen/notas</a>. Contato <a href="mailto:phkonzen@gmail.com?Subject=[Notas]" target="_top"><span class="glyphicon glyphicon-envelope"></span></a>
</div>
</div>

</div>
</div>

  </body>
</html>
