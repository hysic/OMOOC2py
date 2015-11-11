<p>Welcome to the Web diary by hysic.</p>
<p>输入 clear 清空日记.慎用!!!</p>

<form action='/diary' method="POST">
	<input type="text" size="100" maxlength="100" name="new_line" autofocus>
	<input type="submit" name="save" value="保存">
</form>

<div>
%with open(diary_file) as f:
  %for line in f:
    <p>{{line}}</p>
  %end
%end
</div>