namespace SampleConsoleApp;
public sealed class TodoConsoleApp
{
    private readonly TodoService _todos = new();
    public void Run()
    {
        Console.WriteLine("Sample To-Do Console App (.NET 8)");
        while (true)
        {
            Console.WriteLine("1 List | 2 Add | 3 Complete | 4 Delete | 0 Exit");
            Console.Write("Choice: "); var choice = Console.ReadLine()?.Trim();
            switch (choice)
            {
                case "1": foreach (var x in _todos.GetAll()) Console.WriteLine($"[{(x.IsComplete ? "x" : " ")}] {x.Id}: {x.Title}"); break;
                case "2": Console.Write("Title: "); try { Console.WriteLine($"Added #{_todos.Add(Console.ReadLine() ?? "").Id}"); } catch (ArgumentException e) { Console.WriteLine(e.Message); } break;
                case "3": Act("ID to complete: ", _todos.Complete); break;
                case "4": Act("ID to delete: ", _todos.Delete); break;
                case "0": return;
                default: Console.WriteLine("Choose 0–4."); break;
            }
        }
    }
    private static void Act(string prompt, Func<int,bool> operation)
    { Console.Write(prompt); if (int.TryParse(Console.ReadLine(), out var id)) Console.WriteLine(operation(id) ? "Done." : "Item not found."); else Console.WriteLine("Enter a numeric ID."); }
}
