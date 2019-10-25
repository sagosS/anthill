#!/usr/bin/env bash
if [[ -n "$1" ]]
then

    if [[ "$1" == "-start" ]]
    then
        if [[ -n "$2" ]]
        then
            source venv/bin/activate
            python3 app.py $2
            deactivate
        else
            echo " Укажите параметры для start."
            echo ""
        fi
    fi

    if [[ "$1" == "-crontab" ]]
    then
        if [[ -n "$2" ]]
            then
                if [[ "$2" == "--list" ]]
                then
                    crontab -l
                elif [[ "$2" == "--redactor" ]]
                then
                    crontab -e
                elif [[ "$2" == "--delete" ]]
                then
                    crontab -r
                elif [[ "$2" == "--write" ]]
                then
                    crontab -r
                    command="cd first/ && bash run.sh -start startDay"
                    job="0 7 * * * $command"
                    cat <(fgrep -i -v "$command" <(crontab -l)) <(echo "$job") | crontab -

                    command="cd first/ && bash run.sh -start WVCF"
                    job="5 7 * * * $command"
                    cat <(fgrep -i -v "$command" <(crontab -l)) <(echo "$job") | crontab -

                    command="cd first/ && bash run.sh -start holidayNow"
                    job="0 9 * * * $command"
                    cat <(fgrep -i -v "$command" <(crontab -l)) <(echo "$job") | crontab -

                    command="cd first/ && bash run.sh -start weatherNow"
                    job="0 12 * * * $command"
                    cat <(fgrep -i -v "$command" <(crontab -l)) <(echo "$job") | crontab -

                    command="cd first/ && bash run.sh -start holidayPre"
                    job="0 16 * * * $command"
                    cat <(fgrep -i -v "$command" <(crontab -l)) <(echo "$job") | crontab -
                    crontab -l

                    echo '>> crontab создан'
                fi
            else
                echo " Укажите параметры для crontab. "
                echo ""
                echo "  --list     | Вывести содержимое текущего файла расписания"
                echo "  --redactor | Редактирование текущего файла расписания"
                echo "  --delete   | Удаление текущего файла расписания"
                echo "  --write    | Записать задание в crontab"
                echo ""
        fi
    fi

    if [[ "$1" == "-pip" ]]
    then
        if [[ -n "$2" ]]
            then
                if [[ "$2" == "--install" ]]
                then
                    source venv/bin/activate
                    pip3 install -r requirements.txt
                    deactivate
                    echo '>> requirements удачно установлен'
                elif [[ "$2" == "--freeze" ]]
                then
                    source venv/bin/activate
                    pip3 freeze > requirements.txt
                    deactivate
                    echo '>> requirements.txt удачно записан'
                fi
            else
                echo " Укажите параметры для pip. "
                echo ""
                echo "  --install | Установить pip зависимосьти"
                echo "  --freeze  | Создать requirements.txt"
                echo ""
        fi
    fi

else
echo " Укажите параметры для run."
echo ""
echo "  -start   | Запуск приложения с параметрами"
echo "  -crontab | Работа с планировщиком заданий"
echo "  -pip     | Работа с зависимостями"
echo ""
fi
