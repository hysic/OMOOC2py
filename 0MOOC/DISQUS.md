# DISQUS 私人教程

配置DISQUS我偷了个懒，找到上一期OMOOCpy前辈的[教程](https://openmindclub.gitbooks.io/omooc-py/content/support/Disqus_Setup.html)，说的已经很详细了。唯一的区别是我在 `book.json` 中的内容如下：

```javasctipt
{
    "plugins": [
        "disqus"
    ],
    "pluginsConfig": {
    	"disqus":{
    		"shortName": "hysic"
    	}
    }
}
```

