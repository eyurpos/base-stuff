create_files()
{
    mkdir tmp
    touch tmp/a.txt
    touch tmp/ab.txt
    touch tmp/b.txt
    touch tmp/a.file
    touch tmp/ab.file
    touch tmp/b.file

    ls tmp
}

delete_files()
{
    ls tmp

    rm -rf tmp
}

if [ "$1" = "C" ]; then
    create_files
elif [ $1 = "D" ]; then
    delete_files
fi