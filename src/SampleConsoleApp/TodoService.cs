namespace SampleConsoleApp;
public sealed class TodoService
{
    private readonly List<TodoItem> _items = [];
    private int _nextId = 1;
    public IReadOnlyList<TodoItem> GetAll() => _items.AsReadOnly();
    public TodoItem Add(string title)
    {
        if (string.IsNullOrWhiteSpace(title)) throw new ArgumentException("Title is required.", nameof(title));
        var item = new TodoItem(_nextId++, title.Trim()); _items.Add(item); return item;
    }
    public bool Complete(int id)
    {
        var index = _items.FindIndex(x => x.Id == id); if (index < 0) return false;
        _items[index] = _items[index] with { IsComplete = true }; return true;
    }
    public bool Delete(int id) => _items.RemoveAll(x => x.Id == id) > 0;
}
