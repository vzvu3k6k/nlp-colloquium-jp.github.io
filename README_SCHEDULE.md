# 講演者リストについて

- `_schedule`: ここにデータを置く
- `_includes/schedule.html`: HTML
- `_sass/_layout.scss`: CSS

# マークダウンファイルのフィールド

- `layout: post`: デフォルト
- `inline: true`: デフォルト (`false` にすると個別ベージを作ることができるが未対応)
- `date`: 日時 (JST=`+0900`) (例: `2021-09-08 12:30:00+0900`)
- `date_em`: 日付を強調表示するとき `true`
- `time_em`: 時間を強調表示するとき `true`
- `name`: 講演者の名前
- `affiliation`: 所属
- `bio`: スピーカー紹介 (現在非表示)
- `website`: スピーカー名前からリンクするWebサイト
- `topic`: 講演のタイトル
- `abstract`: 講演の概要
- `display`: `true` で表示 / `false` で非表示

## Tips

- 文字列の中に `:` のような表示できない文字がある場合、文字列全体をダブルクオーテーション `"` で囲む。 (例: `_schedule/2021-04-21_akari-asai.md`)

