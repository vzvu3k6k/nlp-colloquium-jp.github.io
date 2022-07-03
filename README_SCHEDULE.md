# 講演者リストについて

- `_schedule`: ここにデータを置く
- `_includes/schedule.html`: 一覧表HTML
- `_layouts/talk.html`: 個別ページHTML
- `_sass/_layout.scss`: CSS

# マークダウンファイルのフィールド

- `layout: talk [defult]`: `_layouts/talk.html` を使ってページを生成するという意味。特別な理由がない限り変更しないこと。
- `inline: false [default]`: `true` かつ `abstract` にテキストが入っているとき、一覧表の中で概要を表示する。それ以外の場合は個別ベージを生成する。
- `date`: 日時 (JST=`+0900`) (例: `2021-09-08 12:30:00+0900`)
- `date_em`: 日付を強調表示するとき `true`
- `time_em`: 時間を強調表示するとき `true`
- `date_tba`: 日時が未定 (TBA) のとき `true` (`date_tba==true` のとき、時間も非表示になる)
- `time_tba`: 時間が未定 (TBA) のとき `true`
- `name`: 講演者の名前
- `affiliation`: 所属
- `bio`: スピーカー紹介 (現在非表示)
- `website`: スピーカー名前からリンクするWebサイト
- `topic`: 講演のタイトル
- `abstract`: 講演の概要
- `display`: `true` で表示 / `false` で非表示

## Tips

- 文字列の中に `:` のような表示できない文字がある場合、文字列全体をダブルクオーテーション `"` で囲む。 (例: `_schedule/2021-04-21_akari-asai.md`)

