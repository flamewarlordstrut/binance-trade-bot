# Как загрузить проект и выпустить релиз

## 1. Названия

| Поле | Значение |
| --- | --- |
| Репозиторий | `binance-trade-bot-windows` |
| About → Description | `Independent fork of ccxt/binance-trade-bot with Windows downloads via GitHub Releases.` |
| Topics | `python`, `binance`, `trading-bot`, `cryptocurrency`, `windows` |
| Тег первого проверенного выпуска | `v1.0.0` |
| Заголовок релиза | `Binance Trade Bot v1.0.0 — Windows x64 (Independent Fork)` |
| Имя приложения | `binance-trade-bot-windows-x64.exe` |
| Конфигурация в релизе | `user.cfg.example` |
| Список монет в релизе | `supported_coin_list` |
| Контрольные суммы | `SHA256SUMS.txt` |

Название `.exe` рассчитано на приложение для Windows x64. Для другой архитектуры исправь название и ссылки. Суффикс `setup` не используется: в этом комплекте нет установщика.

## 2. Подставь свой аккаунт

В `README.md` и `RELEASE_NOTES.md` замени `YOUR_GITHUB_USERNAME` на свой GitHub-логин. Если выберешь другое имя репозитория, исправь в ссылках и `binance-trade-bot-windows`.

Можно сделать это автоматически из папки проекта, если установлен Python:

```text
python tools/configure_repository.py ТВОЙ_ЛОГИН
```

Для другого имени репозитория:

```text
python tools/configure_repository.py ТВОЙ_ЛОГИН ИМЯ_РЕПОЗИТОРИЯ
```

Внешние ссылки на исходный проект менять не нужно.

## 3. Залей исходники

Предпочтительный вариант — сделать Fork оригинала `https://github.com/ccxt/binance-trade-bot`, переименовать форк и добавить подготовленные файлы поверх него. Так сохранится история оригинала.

Также можно создать пустой публичный репозиторий и загрузить **содержимое распакованной папки**, чтобы `README.md`, `LICENSE` и `binance_trade_bot` лежали в корне. ZIP сам по себе GitHub не распакует. Сохрани скрытые файлы, в частности `.user.cfg.example` и `.gitignore`; через GitHub Desktop это удобнее. Не загружай свои ключи, рабочий `user.cfg`, базы или логи.

В комплекте сохранены исходники оригинала, лицензия и исходный README. Документация явно обозначает независимый форк.

## 4. Подготовь настоящий Windows-выпуск

Готового `.exe` в этом комплекте **нет**. Сборка под Windows и её запуск не выполнялись. Зависимости оригинала оставлены без обновления; совместимость со свежими Python, Windows и API биржи не проверена. В исходном `requirements.txt` присутствуют устаревшие и потенциально конфликтующие версии, поэтому считать установку и сборку готовыми нельзя.

Для релиза используй исполняемый файл, собранный из кода соответствующего тега. Простое переименование другого файла не превращает его в сборку этого проекта. Если твоя сборка требует дополнительные DLL или папки, включи их в отдельный ZIP и скорректируй README и описание релиза под фактический комплект.

После сборки проверь на Windows запуск, чтение конфигурации, наличие нужных файлов и работу в тестовом окружении. В релиз публикуй только описание реально проверенных возможностей. Если это предварительная версия, используй тег вроде `v1.0.0-beta.1`, отметь **Pre-release** и замени ссылки `/releases/latest` на страницу конкретного релиза `/releases/tag/v1.0.0-beta.1`.

Скопируй из проекта `.user.cfg.example` и назови копию `user.cfg.example` — это имя используется для вложения релиза. Исходный скрытый файл сохрани в репозитории. Скопируй также `supported_coin_list`, предварительно проверив его актуальность для своей сборки.

## 5. Создай контрольные суммы

Положи три файла будущего релиза в одну отдельную папку: `.exe`, `user.cfg.example` и `supported_coin_list`. Открой там PowerShell:

```powershell
$releaseFiles = @('binance-trade-bot-windows-x64.exe', 'user.cfg.example', 'supported_coin_list')
$checksumLines = foreach ($releaseFile in $releaseFiles) {
    $fileHash = (Get-FileHash -LiteralPath $releaseFile -Algorithm SHA256).Hash.ToLowerInvariant()
    "$fileHash  $releaseFile"
}
$checksumLines | Set-Content -LiteralPath SHA256SUMS.txt -Encoding ascii
```

Здесь считаются суммы именно твоих файлов; фиктивных готовых сумм в комплекте нет.

## 6. Опубликуй релиз

1. Открой свой репозиторий → **Releases** → **Create a new release** / **Draft a new release**.
2. Создай тег `v1.0.0` на коммите с опубликованными исходниками этой сборки.
3. Вставь заголовок из таблицы выше.
4. Скопируй содержимое `RELEASE_NOTES.md` в описание. Проверь, что названия файлов и инструкция совпадают с твоей сборкой.
5. Прикрепи четыре файла: `binance-trade-bot-windows-x64.exe`, `user.cfg.example`, `supported_coin_list`, `SHA256SUMS.txt`.
6. Для проверенного обычного выпуска выбери **Set as latest release** и нажми **Publish release**. До готовности можно сохранить черновик.
7. Проверь ссылку скачивания из README в браузере без входа в аккаунт.

## 7. Ссылки для трафика

Страница последнего обычного релиза:

```text
https://github.com/ТВОЙ_ЛОГИН/binance-trade-bot-windows/releases/latest
```

Прямая ссылка на файл:

```text
https://github.com/ТВОЙ_ЛОГИН/binance-trade-bot-windows/releases/latest/download/binance-trade-bot-windows-x64.exe
```

Сохраняй имя файла при следующих выпусках. До публикации обычного релиза с таким вложением прямая ссылка не заработает. GitHub продолжит предоставлять исходники через Download ZIP и Source code; сам `.exe` можно размещать только в Releases.

## Справка

- Создание релиза: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- Ссылки на релизы: https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases
- Загрузка файлов: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
