# Фабричный метод и его реализация на Python 
<br>  Фабричный метод это порождающий паттерн. Это шаблон проектирования, который создает 
объекты с общим интерфейсом.<br>
  Он отделяет процесс создания объекта от кода который определеяет интерфейс объекта.
  Например, приложению требуется объект с определенным интерфейсом для выполнения своих 
  задач. Конкретная реализация интерфейса идентифицируется некоторым параметром. 
  Вместо использования сложной условной структуры if / elif / else для определения 
  конкретной реализации приложение делегирует это решение отдельному компоненту, 
  который создает конкретный объект. При таком подходе код приложения упрощается, 
  что делает его более пригодным для повторного использования и упрощением обслуживания.
<br> Фабричный метод можно разделить на три уровня:<br> 
