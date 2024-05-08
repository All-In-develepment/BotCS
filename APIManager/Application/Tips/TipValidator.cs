using Domain;
using FluentValidation;

namespace Application.Tips
{
    public class TipValidator : AbstractValidator<Tip>
    {
        public TipValidator()
        {
            RuleFor(x => x.TipMatchId).NotEmpty();
            RuleFor(x => x.TipMaps).NotEmpty();
            RuleFor(x => x.TeamA).NotEmpty();
            RuleFor(x => x.TeamB).NotEmpty();
            RuleFor(x => x.FavoriteTeam).NotEmpty();
            RuleFor(x => x.TipMapOdd).NotEmpty();
            RuleFor(x => x.TipStatus).NotEmpty();
        }
    }
}