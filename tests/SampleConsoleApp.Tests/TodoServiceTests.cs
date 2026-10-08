using SampleConsoleApp;
using Xunit;
public class TodoServiceTests
{
    [Fact] public void Add_TrimsTitleAndAssignsId() { var s=new TodoService(); var x=s.Add(" task "); Assert.Equal(1,x.Id); Assert.Equal("task",x.Title); }
    [Fact] public void Add_RejectsBlankTitle() { Assert.Throws<ArgumentException>(()=>new TodoService().Add(" ")); }
    [Fact] public void Complete_ChangesStatusAndUnknownIdReturnsFalse() { var s=new TodoService(); var x=s.Add("task"); Assert.True(s.Complete(x.Id)); Assert.True(s.GetAll()[0].IsComplete); Assert.False(s.Complete(99)); }
    [Fact] public void Delete_RemovesExistingItem() { var s=new TodoService(); var x=s.Add("task"); Assert.True(s.Delete(x.Id)); Assert.Empty(s.GetAll()); }
}
