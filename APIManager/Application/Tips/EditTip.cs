using Application.Core;
using Domain;
using FluentValidation;
using MediatR;
using Persistence;

namespace Application.Tips
{
    public class EditTip
    {
        public class Command : IRequest<Result<Unit>>
        {
            public Tip Tip { get; set; }
        }

        public class CommandValidator : AbstractValidator<Command>
        {
            public CommandValidator()
            {
                RuleFor(x => x.Tip).SetValidator(new TipValidator());
            }

            public class Handler : IRequestHandler<Command, Result<Unit>>
            {
                private readonly DataContext _context;
                public Handler(DataContext context)
                {
                    _context = context;
                }

                public async Task<Result<Unit>> Handle(Command request, CancellationToken cancellationToken)
                {
                    var tip = await _context.Tips.FindAsync(request.Tip.TipMatchId);

                    if (tip == null) return null;

                    tip.TipMatchId = request.Tip.TipMatchId;
                    tip.TeamA = request.Tip.TeamA;
                    tip.TeamB = request.Tip.TeamB;
                    tip.FavoriteTeam = request.Tip.FavoriteTeam;
                    tip.TipMaps = request.Tip.TipMaps;
                    tip.TipMapOdd = request.Tip.TipMapOdd;
                    tip.TipMessageId = request.Tip.TipMessageId;
                    tip.TipsMapResult = request.Tip.TipsMapResult;
                    tip.TipDate = request.Tip.TipDate;
                    tip.TipStatus = request.Tip.TipStatus;

                    var result = await _context.SaveChangesAsync() > 0;

                    if (!result) return Result<Unit>.Failure("Failed to update tip");

                    return Result<Unit>.Success(Unit.Value);
                }
            }
        }
    }
}